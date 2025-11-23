import { render, screen, fireEvent } from '@testing-library/react';
import QueryForm from '../QueryForm';

test('renders QueryForm and disables submit on empty', () => {
  render(<QueryForm onSubmit={() => {}} />);
  expect(screen.getByRole('button')).toBeDisabled();
});

test('calls onSubmit with query', () => {
  const onSubmit = jest.fn();
  render(<QueryForm onSubmit={onSubmit} />);
  fireEvent.change(screen.getByRole('textbox'), { target: { value: 'Test query' } });
  fireEvent.click(screen.getByRole('button'));
  expect(onSubmit).toHaveBeenCalledWith('Test query');
});
