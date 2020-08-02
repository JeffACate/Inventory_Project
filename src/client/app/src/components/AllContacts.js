import React, { useEffect, useState }  from 'react';

export default function AllContacts() {
    const [contacts, getContacts] = useState(null);
    const [rows, getRows] = useState(null);

    useEffect(() => {
        fetchContacts();

        async function fetchContacts() {
            try{
                const res = await fetch('http://localhost:5000/api/contacts/all');
                const data = await res.json();
                getContacts(data);
            }catch{
                console.error();
            }
        }
    }, []);

    function getRows(){
        // console.log('data', data);
        console.log('contacts',contacts);
        if (contacts){
            contacts.forEach(contact => {
                rows.push(<tr>
                            <td>{contact['id']}</td>
                            <td>{contact['first']}</td>
                            <td>{contact['last']}</td>
                            <td>{contact['year']}</td>
                        </tr>);
            });
        }
    }

    return (
        <>
            <div className="row justify-content-center">
                <h2 className="display-4">Contacts</h2>
            </div>
            <div className="row">
                <table className="table text-center table-dark">
                    <thead>
                        <tr>
                            <th>ID</th>
                            <th>FIRST</th>
                            <th>LAST</th>
                            <th>BIRTH YEAR</th>
                        </tr>
                    </thead>
                    <tbody>
                        {getRows()}
                    </tbody>
                </table>
                
            </div>
        </>
    )
}