import { Link, useParams } from 'react-router-dom';
import { Subject } from '../types';

interface SidebarProps {
  subject: Subject;
}

const Sidebar = ({ subject }: SidebarProps) => {
  const { unitId } = useParams();

  return (
    <div className="w-64 bg-gray-50 border-r h-full overflow-y-auto hidden md:block">
      <div className="p-4 border-b">
        <h2 className="font-semibold text-lg text-gray-800">{subject.title}</h2>
        <Link to={`/subject/${subject.id}`} className="text-sm text-blue-600 hover:underline">
          Back to Overview
        </Link>
      </div>
      <div className="p-4">
        <h3 className="text-xs font-semibold text-gray-500 uppercase tracking-wider mb-2">Units</h3>
        <nav className="space-y-1">
          {subject.units?.map((unit) => (
            <Link
              key={unit.id}
              to={`/subject/${subject.id}/unit/${unit.id}`}
              className={`block px-3 py-2 text-sm font-medium rounded-md ${
                Number(unitId) === unit.id
                  ? 'bg-blue-100 text-blue-700'
                  : 'text-gray-700 hover:bg-gray-100 hover:text-gray-900'
              }`}
            >
              {unit.title}
            </Link>
          ))}
          <div className="pt-4">
             <Link
                to={`/subject/${subject.id}/create-unit`}
                className="flex items-center justify-center w-full px-4 py-2 text-sm font-medium text-white bg-blue-600 rounded-md hover:bg-blue-700 focus:outline-none focus:ring-2 focus:ring-offset-2 focus:ring-blue-500"
              >
                + New Unit
            </Link>
          </div>
        </nav>
      </div>
    </div>
  );
};

export default Sidebar;

