import React from 'react';

export default function Home() {
    return (
        <>
            {/* row */}
            <div className="row pt-2 justify-content-center" hidden>
                <h1>Inventory App</h1>
            </div>
            {/* row */}
            <div className="row">
                {/* column */}
                <div id="carouselExampleSlidesOnly" className=" col-sm-6  carousel slide w-50 h-75" data-ride="carousel">
                    <ol className="carousel-indicators">
                        <li data-target="#carouselExampleIndicators" data-slide-to="0" ></li>
                        <li data-target="#carouselExampleIndicators" data-slide-to="1" className="active"></li>
                        <li data-target="#carouselExampleIndicators" data-slide-to="2"></li>
                    </ol>
                    <div className="carousel-inner">
                        <div className="carousel-item">
                            <img className="d-block w-100" src="../../img/inventory.jpg" alt="First slide" />
                        </div>
                        <div className="carousel-item active">
                            <img className="d-block w-100" src="../../img/02-movie-library.jpg" alt="Second slide" />
                        </div>
                        <div className="carousel-item">
                            <img className="d-block w-100" src="../../img/03-a-track.jpg" alt="Third slide" />
                        </div>
                    </div>
                </div>
                {/* column */}
                <div className="col-sm-6">
                    <p>
                        I started this endeavor after a phone interview with a company where 
                        I am currently pursuing employment. I was informed, during the interview, 
                        of the exciting opportunities in this company for continued education. 
                        I got the feeling that the endless pursuit of education was of great value to this
                        company. I learned of the company-hosted hackathons and instantly I wanted 
                        to know more. It was at this moment that inspired me to build a full-stack 
                        application to display my excitement for learning new languages and concepts. 
                        Therefore, having used JavaScript in the past and knowing its increasing popularity 
                        I decided to use React.js for the front-end. Furthermore, I had read a lot 
                        about Python for web development and decided to find out first hand by using
                        Flask to create an API and pyodcbc, a Python ODBC bridge, to connect to the 
                        database.
                    </p>
                </div>
            </div>
        </>
    );
}