import React, { useEffect, useState }  from 'react';

export default function AllContacts() {
    const [contacts, getContacts] = useState(null);

    useEffect(() => {
        fetchContacts();

        async function fetchContacts() {
            try{
                const res = await fetch('http://localhost:5000/api/contacts/all');
                const data = await res.json();
                getContacts(data);
                console.log(data);
            }catch{
                console.error();
            }
        }

    }, []);

    if(contacts == null) {
        return (
        <>
            <h1>AllContacts.js rendered with NO Data!!</h1>
        </>
        

    )}else{

    
    return (
        <>
        <div>
            <h1>"Hello World" from AllContacts.js</h1>
        </div>
        </>
    )}
}