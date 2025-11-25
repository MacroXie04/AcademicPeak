import { ReactNode, useEffect, useState } from 'react';
import { useParams } from 'react-router-dom';
import Sidebar from './Sidebar';
import { getSubject } from '../api/client';
import { Subject } from '../types';

interface LayoutProps {
  children: ReactNode;
}

const Layout = ({ children }: LayoutProps) => {
  const { subjectId } = useParams();
  const [subject, setSubject] = useState<Subject | null>(null);

  useEffect(() => {
    if (subjectId) {
      getSubject(Number(subjectId)).then(setSubject);
    }
  }, [subjectId]);

  return (
    <div className="flex h-screen bg-white">
      {subject && <Sidebar subject={subject} />}
      <div className="flex-1 flex flex-col min-w-0 overflow-hidden">
        <header className="bg-white border-b px-6 py-4 flex items-center justify-between">
           <div className="text-xl font-bold text-gray-900">
               {subject ? subject.title : 'SkillLoop Content Framework'}
           </div>
        </header>
        <main className="flex-1 overflow-y-auto p-6">
          {children}
        </main>
      </div>
    </div>
  );
};

export default Layout;

