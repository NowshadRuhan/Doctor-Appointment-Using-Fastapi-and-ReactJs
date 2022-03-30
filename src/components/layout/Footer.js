import React from 'react';
import { Link } from 'react-router-dom';

const Footer = () =>{

    return (
       <div className="footer-container">
            <h4 className='footer-text'>Powered By:  
            <Link  to="https://nowshadruhan.globentrust.com"  target='_blank'>Nowshad Ruhan</Link></h4>
        </div>
    );

}


export default Footer;