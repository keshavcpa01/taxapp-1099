import React from 'react';
import { useForm } from 'react-hook-form';
import axios from 'axios';

const Login = () => {
  const { register, handleSubmit } = useForm();

  const onSubmit = async (data: any) => {
    const res = await axios.post(`${process.env.REACT_APP_API_BASE_URL}/auth/login`, new URLSearchParams(data));
    localStorage.setItem('token', res.data.access_token);
    alert("Logged in!");
  };

  return (
    <form onSubmit={handleSubmit(onSubmit)} className="max-w-md mx-auto p-4 bg-white shadow rounded space-y-4">
      <input {...register('username')} placeholder="Username" className="w-full border p-2 rounded" />
      <input {...register('password')} type="password" placeholder="Password" className="w-full border p-2 rounded" />
      <button type="submit" className="bg-blue-600 text-white px-4 py-2 rounded hover:bg-blue-700 w-full">Login</button>
    </form>
  );
};

export default Login;
