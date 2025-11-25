import { useEffect, useState } from 'react';
import { Link } from 'react-router-dom';
import { createSubject, getSubjects } from '../api/client';
import { Subject } from '../types';

const HomePage = () => {
  const [subjects, setSubjects] = useState<Subject[]>([]);
  const [newSubjectTitle, setNewSubjectTitle] = useState('');
  const [isCreating, setIsCreating] = useState(false);

  useEffect(() => {
    loadSubjects();
  }, []);

  const loadSubjects = () => {
    getSubjects().then(setSubjects);
  };

  const handleCreateSubject = async (e: React.FormEvent) => {
    e.preventDefault();
    if (!newSubjectTitle.trim()) return;

    setIsCreating(true);
    try {
      await createSubject({ title: newSubjectTitle, description: '' });
      setNewSubjectTitle('');
      loadSubjects();
    } catch (error) {
      console.error("Failed to create subject", error);
    } finally {
      setIsCreating(false);
    }
  };

  return (
    <div className="min-h-screen bg-gray-100 py-12 px-4 sm:px-6 lg:px-8">
      <div className="max-w-3xl mx-auto">
        <div className="text-center mb-12">
          <h1 className="text-4xl font-extrabold text-gray-900 sm:text-5xl sm:tracking-tight lg:text-6xl">
            SkillLoop Content
          </h1>
          <p className="mt-5 max-w-xl mx-auto text-xl text-gray-500">
            Create and manage rich educational content.
          </p>
        </div>

        <div className="bg-white shadow rounded-lg p-6 mb-8">
          <h2 className="text-lg font-medium text-gray-900 mb-4">Create New Subject</h2>
          <form onSubmit={handleCreateSubject} className="flex gap-4">
            <input
              type="text"
              value={newSubjectTitle}
              onChange={(e) => setNewSubjectTitle(e.target.value)}
              placeholder="Subject Title"
              className="flex-1 rounded-md border-gray-300 shadow-sm focus:border-blue-500 focus:ring-blue-500 sm:text-sm border p-2"
            />
            <button
              type="submit"
              disabled={isCreating}
              className="inline-flex items-center px-4 py-2 border border-transparent text-sm font-medium rounded-md shadow-sm text-white bg-blue-600 hover:bg-blue-700 focus:outline-none focus:ring-2 focus:ring-offset-2 focus:ring-blue-500 disabled:opacity-50"
            >
              {isCreating ? 'Creating...' : 'Create'}
            </button>
          </form>
        </div>

        <div className="grid gap-4 sm:grid-cols-2 lg:grid-cols-3">
          {subjects.map((subject) => (
            <Link
              key={subject.id}
              to={`/subject/${subject.id}`}
              className="block bg-white rounded-lg shadow hover:shadow-md transition-shadow p-6"
            >
              <h3 className="text-lg font-medium text-gray-900 truncate">{subject.title}</h3>
              <p className="mt-1 text-sm text-gray-500">
                {subject.units?.length || 0} units
              </p>
            </Link>
          ))}
        </div>
      </div>
    </div>
  );
};

export default HomePage;

