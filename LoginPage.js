import React, { useState } from 'react';
import './App.css';
import axios from 'axios';

function App() {
  const [userId, setUserId] = useState('');
  const [password, setPassword] = useState('');

  const handleSubmit = (event) => {
    event.preventDefault();
    console.log(`User ID: ${userId}, Password: ${password}`);
    axios.post('http://localhost:5000/login', {
      userId: userId,
      password: password
    })
    .then(function (response) {
      console.log(response.data);
    })
    .catch(function (error) {
      console.log(error);
    });
  };

  return (
    <div className="background">
      <div className="container">
        <h1>Login</h1>
        <form onSubmit={handleSubmit}>
          <div className="form-group">
            <label htmlFor="userId">User ID:</label>
            <input type="text" id="userId" name="userId" value={userId} onChange={(e) => setUserId(e.target.value)} placeholder="Enter your User ID" required />
          </div>
          <div className="form-group">
            <label htmlFor="password">Password:</label>
            <input type="password" id="password" name="password" value={password} onChange={(e) => setPassword(e.target.value)} placeholder="Enter your Password" required />
          </div>
          <div className="form-group forgot-password">
            <a href="#">Forgot Password?</a>
          </div>
          <button type="submit">Login</button>
        </form>
      </div>
    </div>
  );
}

export default App;
