import { BrowserRouter as Router, Routes, Route, Navigate } from 'react-router-dom';
import HomePage from './pages/HomePage';
import SubjectPage from './pages/SubjectPage';
import UnitPage from './pages/UnitPage';

function App() {
  return (
    <Router>
      <Routes>
        <Route path="/" element={<HomePage />} />
        <Route path="/subject/:subjectId" element={<SubjectPage />} />
        <Route path="/subject/:subjectId/unit/:unitId" element={<UnitPage />} />
        <Route path="/subject/:subjectId/create-unit" element={<UnitPage />} />
        <Route path="*" element={<Navigate to="/" replace />} />
      </Routes>
    </Router>
  );
}

export default App;
