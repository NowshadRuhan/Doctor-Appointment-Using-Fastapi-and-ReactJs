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
import { useState } from 'react';
import axios from 'axios';


function App() {

  const [users, setUsers] = useState([])
  const [user, setUser] = useState({})

  const fetchUsers = async () =>{
      const  responce = await axios.get('http://127.0.0.1:8000/')
      return setUsers(responce.data)
  }

  // fetchUsers()

  const fetchUser = async (id) =>{
    const  responce = await axios.get(`ttp://127.0.0.1:8000/${id}`)
    return setUsers(responce.data)
  } 

  const createorEditUser = async (id) =>{
    if(user.id){
      await axios.put(`ttp://127.0.0.1:8000/${id}`, user)
    }else{
      await axios.post(`ttp://127.0.0.1:8000/`, user)
    }
    await fetchUsers()
    await setUsers({id: 0, name: '', user_name:'', email: '', password: '', status:''})
    // return setUsers(responce.data)
  } 

  const deteleUser = async (id) =>{
    const  responce = await axios.delete(`ttp://127.0.0.1:8000/${id}`)
    await fetchUsers()
  } 

  

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

     {/* <Footer /> */}
      
    </div>
    </Router>
  );
}

export default App;
