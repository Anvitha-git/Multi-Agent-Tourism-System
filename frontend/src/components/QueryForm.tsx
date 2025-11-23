import React, { useState } from 'react';

interface Props {
  onSubmit: (query: string) => void;
  disabled?: boolean;
}

const QueryForm: React.FC<Props> = ({ onSubmit, disabled }) => {
  const [query, setQuery] = useState('');

  const handleSubmit = (e: React.FormEvent) => {
    e.preventDefault();
    if (!query.trim()) return;
    onSubmit(query.trim());
  };

  return (
    <form onSubmit={handleSubmit} className="space-y-3">
      <textarea
        className="travel-input resize-none"
        rows={3}
        value={query}
        onChange={e => setQuery(e.target.value)}
        placeholder="E.g. I’m going to go to Bangalore, what is the temperature there?"
        disabled={disabled}
      />
      {/* Checkboxes removed: intent now inferred automatically in backend */}
      <button
        type="submit"
        className="travel-btn-primary w-full disabled:opacity-60"
        disabled={disabled || !query.trim()}
      >
        Submit
      </button>
    </form>
  );
};

export default QueryForm;
