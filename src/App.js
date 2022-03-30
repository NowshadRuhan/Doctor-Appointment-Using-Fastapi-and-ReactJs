import React from 'react';
import { BrowserRouter as Router, Route, Routes } from 'react-router-dom';
import '../node_modules/bootstrap/dist/css/bootstrap.css';
import './App.css';
import Navbar from './components/layout/Navbar';
import Home from './components/pages/Home';
import NotFound from './components/pages/NotFound';
import Signin from './components/pages/Signin';
import Signup from './components/pages/Signup';
import Footer from './components/layout/Footer';

function App() {
  return (
    <Router> 
    <div className="App">
      <Navbar />
     <Routes>
        <Route exact path="/" element={<Home />} />
        
        <Route exact path="/Signin" element={<Signin />} />

        <Route exact path="/Signup" element={<Signup />} />

        <Route path='*' exact={true} element={<NotFound />} />
        
     </Routes> 

     <Footer />
      
    </div>
    </Router>
  );
}

export default App;
