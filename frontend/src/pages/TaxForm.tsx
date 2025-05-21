import React from 'react';
import { useForm } from 'react-hook-form';
import axios from 'axios';

const TaxForm = () => {
  const { register, handleSubmit } = useForm();

  const onSubmit = async (data: any) => {
    const token = localStorage.getItem('token');
    const res = await axios.post(`${process.env.REACT_APP_API_BASE_URL}/submissions/`, data, {
      headers: { Authorization: `Bearer ${token}` }
    });
    alert('Submitted: ' + JSON.stringify(res.data));
  };

  return (
    <form onSubmit={handleSubmit(onSubmit)} className="max-w-md mx-auto p-4 bg-white shadow rounded space-y-4">
      <input {...register('payer_name')} placeholder="Payer Name" className="w-full border p-2 rounded" />
      <input {...register('recipient_name')} placeholder="Recipient Name" className="w-full border p-2 rounded" />
      <input {...register('amount')} placeholder="Amount" className="w-full border p-2 rounded" />
      <button type="submit" className="bg-green-600 text-white px-4 py-2 rounded hover:bg-green-700 w-full">Submit 1099</button>
    </form>
  );
};

export default TaxForm;
