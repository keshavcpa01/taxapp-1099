import React from 'react';
import { Navigate, Route, Routes } from 'react-router-dom';
import Login from './Login';
import Register from './Register';
import SubmissionForm from './SubmissionForm';

const AppRoutes: React.FC = () => {
  return (
    <Routes>
      <Route path="/" element={<Navigate to="/login" replace />} />
      <Route path="/register" element={<Register />} />
      <Route path="/login" element={<Login />} />
      <Route path="/submit" element={<SubmissionForm />} />
      <Route path="*" element={<Navigate to="/login" replace />} />
    </Routes>
  );
};

export default AppRoutes;
