import { useEffect, useState } from 'react';
import { Link, useParams } from 'react-router-dom';
import { getSubject } from '../api/client';
import { Subject } from '../types';
import Layout from '../components/Layout';

const SubjectPage = () => {
  const { subjectId } = useParams();
  const [subject, setSubject] = useState<Subject | null>(null);

  useEffect(() => {
    if (subjectId) {
      getSubject(Number(subjectId)).then(setSubject);
    }
  }, [subjectId]);

  if (!subject) return <Layout><div>Loading...</div></Layout>;

  return (
    <Layout>
      <div className="max-w-4xl mx-auto">
        <h1 className="text-3xl font-bold text-gray-900 mb-4">{subject.title}</h1>
        <p className="text-gray-600 mb-8">{subject.description}</p>
        
        <div className="bg-white shadow overflow-hidden sm:rounded-md">
          <div className="px-4 py-5 sm:px-6 border-b border-gray-200 flex justify-between items-center">
            <h3 className="text-lg leading-6 font-medium text-gray-900">Units</h3>
            <Link
                to={`/subject/${subject.id}/create-unit`}
                className="inline-flex items-center px-3 py-2 border border-transparent text-sm leading-4 font-medium rounded-md text-white bg-blue-600 hover:bg-blue-700 focus:outline-none focus:ring-2 focus:ring-offset-2 focus:ring-blue-500"
            >
                Create Unit
            </Link>
          </div>
          <ul className="divide-y divide-gray-200">
            {subject.units?.map((unit) => (
              <li key={unit.id}>
                <Link
                  to={`/subject/${subject.id}/unit/${unit.id}`}
                  className="block hover:bg-gray-50"
                >
                  <div className="px-4 py-4 sm:px-6">
                    <div className="flex items-center justify-between">
                      <div className="text-sm font-medium text-blue-600 truncate">
                        {unit.title}
                      </div>
                      <div className="ml-2 flex-shrink-0 flex">
                        <span className="px-2 inline-flex text-xs leading-5 font-semibold rounded-full bg-green-100 text-green-800">
                          {new Date(unit.updated_at).toLocaleDateString()}
                        </span>
                      </div>
                    </div>
                  </div>
                </Link>
              </li>
            ))}
            {subject.units?.length === 0 && (
                <li className="px-4 py-4 sm:px-6 text-gray-500 text-center">No units yet. Create one!</li>
            )}
          </ul>
        </div>
      </div>
    </Layout>
  );
};

export default SubjectPage;

