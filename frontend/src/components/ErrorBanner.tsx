import React from 'react';

const ErrorBanner: React.FC<{ message: string }> = ({ message }) => (
  <div className="bg-red-100 text-red-700 p-2 rounded mb-2 mt-2">
    {message}
  </div>
);

export default ErrorBanner;
