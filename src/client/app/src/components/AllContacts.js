import React, { useEffect, useState }  from 'react';


export default function AllContacts() {
    const [contacts, getContacts] = useState(null);

    useEffect(() => {
        fetchContacts();

        async function fetchContacts() {
            const res = await fetch(
                'http://localhost:5000/api/contacts/all'
            );

            const data = await res.json();
            getContacts(data);
            console.log(data);

        }
    }, []);

    if(!contacts) return <div />;

    return (
        <div />
    )
}