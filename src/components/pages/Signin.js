import React from 'react';

const Signin = () =>{

    return (
        <div className='container'>
            <section className="vh-100" >
                    <div className="container h-100">
                        <div className="row d-flex justify-content-center align-items-center h-100">
                        <div className="col-lg-12 col-xl-11">
                            <div className="card text-black" >
                            <div className="card-body p-md-5">
                                <div className="row justify-content-center">
                                <div className="col-md-10 col-lg-6 col-xl-5 order-2 order-lg-1">

                                    <p className="text-center h1 fw-bold mb-5 mx-1 mx-md-4 mt-4">Sign in</p>

                                    <form className="mx-1 mx-md-4" method='POST'>

                                

                                    <div className="d-flex flex-row align-items-center mb-4">
                                        <i className="fas fa-user fa-lg me-3 fa-fw"></i>
                                        <div className="form-outline flex-fill mb-0">
                                        <label className="form-label" for="form3Example1c">User Name</label>
                                        <input type="text" id="form3Example1c" className="form-control" required="" />
                                        </div>
                                    </div>


                                    <div className="d-flex flex-row align-items-center mb-4">
                                        <i className="fas fa-lock fa-lg me-3 fa-fw"></i>
                                        <div className="form-outline flex-fill mb-0">
                                        <label className="form-label" for="form3Example4c">Password</label>
                                        <input type="password" id="form3Example4c" className="form-control" required="" />
                                        {/* <div id="emailHelp" className="form-text">Password must be contain uppercase and lowercase letter, numeric character and special character.</div> */}
                                        </div>
                                    </div>



                                    <div className="d-flex justify-content-center mx-4 mb-3 mb-lg-4">
                                        <button type="button" className="btn btn-primary btn-lg">Login</button>
                                    </div>

                                    </form>

                                </div>
                                <div className="col-md-10 col-lg-6 col-xl-7 d-flex align-items-center order-1 order-lg-2">

                                    <img type="image" src={'https://mdbcdn.b-cdn.net/img/Photos/new-templates/bootstrap-registration/draw1.webp'} className="img-fluid" alt="Sample image" />

                                </div>
                                </div>
                            </div>
                            </div>
                        </div>
                        </div>
                    </div>
                </section>
            </div>

    );

}


export default Signin;