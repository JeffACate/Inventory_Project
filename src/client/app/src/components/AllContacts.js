import React, { useEffect, useState }  from 'react';
import ReactDOM, { render } from "react-dom";

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

    return (
        <>
            <div className="row justify-content-center">
                <h2 className="display-4">Contacts</h2>
            </div>
            <div className="row">
                <table className="table table-striped text-center table-hover table-dark">
                    <thead>
                        <tr>
                            <th scope="col">ID</th>
                            <th scope="col">FIRST</th>
                            <th scope="col">LAST</th>
                            <th scope="col">BIRTH YEAR</th>
                        </tr>
                    </thead>
                    <tbody>
                    </tbody>
                </table>
            </div>
        </>
    )
}   




    
    {/* {this.rows} */}