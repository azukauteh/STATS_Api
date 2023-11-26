import React, { useState } from 'react';

const ProfileUpdateForm = () => {
  // State to manage form fields
  const [formData, setFormData] = useState({
    username: '',
    email: '',
    //more input
  });

  // handle form field changes
  const handleInputChange = (e) => {
    const { name, value } = e.target;
    setFormData((prevData) => ({
      ...prevData,
      [name]: value,
    }));
  };

  // handle form submission
  const handleSubmit = (e) => {
    e.preventDefault();
    // logic to send updated profile info to the server
    console.log('Updating profile:', formData);
  };

  return (
    <div className="profile-update-form">
      <h2>Update Your Profile</h2>
      <form onSubmit={handleSubmit}>
        <label htmlFor="username">Username:</label>
        <input
          type="text"
          id="username"
          name="username"
          value={formData.username}
          onChange={handleInputChange}
        />

        <label htmlFor="email">Email:</label>
        <input
          type="email"
          id="email"
          name="email"
          value={formData.email}
          onChange={handleInputChange}
        />

        {/* Add more*/}

        <button type="submit">Update Profile</button>
      </form>
    </div>
  );
};

export default ProfileUpdateForm;
