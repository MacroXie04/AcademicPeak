import { useEffect, useState } from 'react';
import { useNavigate, useParams } from 'react-router-dom';
import { createUnit, getUnit, updateUnit } from '../api/client';
import RichTextEditor from '../components/RichTextEditor';
import Layout from '../components/Layout';

const UnitPage = () => {
  const { subjectId, unitId } = useParams();
  const navigate = useNavigate();
  const isCreating = !unitId;

  const [title, setTitle] = useState('');
  const [content, setContent] = useState('');
  const [isEditable, setIsEditable] = useState(false);
  const [isLoading, setIsLoading] = useState(false);

  useEffect(() => {
    if (unitId) {
      setIsLoading(true);
      getUnit(Number(unitId)).then((unit) => {
        setTitle(unit.title);
        setContent(unit.content);
        setIsLoading(false);
      });
      setIsEditable(false); // Default to view mode for existing units
    } else {
      setIsEditable(true); // Default to edit mode for new units
    }
  }, [unitId]);

  const handleSave = async () => {
    if (!subjectId) return;
    
    setIsLoading(true);
    try {
      if (isCreating) {
        const newUnit = await createUnit({
          subject: Number(subjectId),
          title,
          content,
        });
        navigate(`/subject/${subjectId}/unit/${newUnit.id}`);
      } else {
        await updateUnit(Number(unitId), {
          title,
          content,
        });
        setIsEditable(false);
      }
    } catch (error) {
      console.error("Failed to save unit", error);
      alert("Failed to save unit");
    } finally {
        setIsLoading(false);
    }
  };

  return (
    <Layout>
      <div className="max-w-4xl mx-auto space-y-6">
        <div className="flex justify-between items-center">
          {isEditable ? (
             <input
              type="text"
              value={title}
              onChange={(e) => setTitle(e.target.value)}
              placeholder="Unit Title"
              className="text-3xl font-bold text-gray-900 border-b border-gray-300 focus:border-blue-500 outline-none w-full py-2 bg-transparent"
            />
          ) : (
            <h1 className="text-3xl font-bold text-gray-900">{title}</h1>
          )}
          
          <div className="flex space-x-3">
             {!isCreating && (
                <button
                  onClick={() => setIsEditable(!isEditable)}
                  className="px-4 py-2 border border-gray-300 rounded-md text-sm font-medium text-gray-700 bg-white hover:bg-gray-50 focus:outline-none"
                >
                  {isEditable ? 'Cancel' : 'Edit'}
                </button>
             )}
            {isEditable && (
              <button
                onClick={handleSave}
                disabled={isLoading}
                className="px-4 py-2 border border-transparent rounded-md shadow-sm text-sm font-medium text-white bg-blue-600 hover:bg-blue-700 focus:outline-none disabled:opacity-50"
              >
                {isLoading ? 'Saving...' : 'Save'}
              </button>
            )}
          </div>
        </div>

        <div className="min-h-[500px]">
           <RichTextEditor
              content={content}
              editable={isEditable}
              onChange={setContent}
            />
        </div>
      </div>
    </Layout>
  );
};

export default UnitPage;

