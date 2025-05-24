import axios from 'axios';
import React from 'react';
import { useForm } from 'react-hook-form';
import { toast } from 'react-toastify';

type FormData = {
    payer_name: string;
    payer_tin: string;
    payer_address: string;
    payer_city: string;
    payer_state: string;
    payer_zip: string;
    payer_email: string;

    recipient_name: string;
    recipient_tin: string;
    recipient_phone: string;
    recipient_address: string;
    recipient_city: string;
    recipient_state: string;
    recipient_zip: string;

    payment_date: string;
    nonemployee_compensation: string;
    federal_income_tax_withheld: string;

    state: string;
    state_id: string;
    state_income: string;
};

const SubmissionForm: React.FC = () => {
    const {
        register,
        handleSubmit,
        reset,
        formState: { errors }
    } = useForm<FormData>();

    const onSubmit = async (data: FormData) => {
        try {
            const token = localStorage.getItem('token');
            await axios.post(`${import.meta.env.VITE_API_BASE_URL}/submissions`, data, {
                headers: {
                    Authorization: `Bearer ${token}`
                }
            });
            toast.success('Submission successful!');
            reset();
        } catch (error) {
            console.error(error);
            toast.error('Submission failed. Please try again.');
        }
    };

    const renderInput = (
        name: keyof FormData,
        label: string,
        type: string = 'text',
        required = true
    ) => (
        <div>
            <input
                {...register(name, { required })}
                type={type}
                placeholder={label}
                className="w-full border rounded px-3 py-2"
            />
            {errors[name] && (
                <p className="text-red-500 text-sm mt-1">{label} is required.</p>
            )}
        </div>
    );

    return (
        <div className="max-w-5xl mx-auto p-6 bg-white rounded shadow">
            <h2 className="text-2xl font-bold mb-6">1099-NEC Submission Form</h2>
            <form onSubmit={handleSubmit(onSubmit)} className="space-y-4">
                <div className="grid grid-cols-2 gap-4">
                    {renderInput('payer_name', 'Payer Name')}
                    {renderInput('payer_tin', 'Payer TIN')}
                    {renderInput('payer_address', 'Payer Address')}
                    {renderInput('payer_city', 'Payer City')}
                    {renderInput('payer_state', 'Payer State')}
                    {renderInput('payer_zip', 'Payer Zip')}
                    {renderInput('payer_email', 'Payer Email')}

                    {renderInput('recipient_name', 'Recipient Name')}
                    {renderInput('recipient_tin', 'Recipient TIN')}
                    {renderInput('recipient_phone', 'Recipient Phone', 'text', false)}
                    {renderInput('recipient_address', 'Recipient Address')}
                    {renderInput('recipient_city', 'Recipient City')}
                    {renderInput('recipient_state', 'Recipient State')}
                    {renderInput('recipient_zip', 'Recipient Zip')}

                    {renderInput('payment_date', 'Payment Date', 'date')}
                    {renderInput('nonemployee_compensation', 'Nonemployee Compensation')}
                    {renderInput('federal_income_tax_withheld', 'Federal Tax Withheld')}

                    {renderInput('state', 'State', 'text', false)}
                    {renderInput('state_id', 'State ID', 'text', false)}
                    {renderInput('state_income', 'State Income', 'text', false)}
                </div>

                <button
                    type="submit"
                    className="bg-blue-600 text-white px-6 py-2 rounded hover:bg-blue-700"
                >
                    Submit 1099
                </button>
            </form>
        </div>
    );
};

export default SubmissionForm;
