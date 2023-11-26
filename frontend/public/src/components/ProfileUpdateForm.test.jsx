// ProfileUpdateForm.test.jsx
import React from 'react';
import { render, screen } from '@testing-library/react';
import ProfileUpdateForm from './ProfileUpdateForm';

test('renders ProfileUpdateForm component', () => {
  render(<ProfileUpdateForm />);
  //assertions based on how the component should behave
  expect(screen.getByText('Your text')).toBeInTheDocument();
});

