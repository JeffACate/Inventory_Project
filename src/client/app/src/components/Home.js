import React from 'react';

export default function Home() {
    return (
        <>
        <div className="row pt-2 justify-content-center" hidden>
            <h1>Inventory App</h1>
        </div>
        <div className="row">
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
            <div className="col-sm-6 text-center align-content-center ">
                <p>Green vines attached to the trunk of the tree had wound themselves toward the top of the <span className=" bg-danger text-white">A PARAGRAPH ABOUT MY PROJECT</span> ottom or bottom to top depending on their current chore. At least this was the way it was supposed to be. Something had damaged the vine overnight halfway up the tree leaving a gap in the once pristine ant highway.</p>
            </div>
        
        </div>
        </>
    );
}