import React from 'react';
import { render } from '@testing-library/react';
import App from './App';

test('renders input', () => {
  const { getByPlaceholderText } = render(<App />);
  const inputElement = getByPlaceholderText(/twitter topic/i);
  expect(inputElement).toBeInTheDocument();
});
