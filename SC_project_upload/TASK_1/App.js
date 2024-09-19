import React from "react";
import axios from "axios";
import { useState } from "react";

function Login() {
  const [password, setPassword] = useState("");
  const [username, setUsername] = useState("");
  const [accessToken, setAccessToken] = useState(null);
  const [productName, setProductName] = useState("");
  const [productDesc, setProductDesc] = useState("");

  const [showLogin, setShowLogin] = useState(false);
  const [showProduct, setShowProduct] = useState(true);
  const [showAdd, setShowAdd] = useState(true);
  const [showGet, setShowGet] = useState(true);
  
  const handleLogin = async (event) => {
    event.preventDefault();
    const data = {
      username: username,
      password: password,
    };
    let axiosConfig = {
  headers: {
      'Content-Type': 'application/json;charset=UTF-8',
      "Access-Control-Allow-Origin": "*",
  }
  };
    try {
      const response = await axios.post("http://localhost:8000/login", data, axiosConfig);
      setAccessToken(response.data.access_token);
      alert("Login successful");
      setShowLogin(true);
      setShowProduct(false);
      
    } catch (error) {
      console.error(error);
      alert("Login Failed : "+ error.response.data['msg']);
    }
  };

  const handleAddProduct = async (event) => {
    event.preventDefault();
    const data = {
      product_name: productName,
      product_desc: productDesc,
      access_token: accessToken,
    };
    let axiosConfig = {
  headers: {
      'Content-Type': 'application/json;charset=UTF-8',
      "Access-Control-Allow-Origin": "*",
  }
  };
    try {
      const response = await axios.post("http://localhost:8000/products", data, axiosConfig);
      alert("Product Added Successfully");
      
    } catch (error) {
      console.error(error);
      alert("Add product has failed : " + error.response.data['msg']);
    }
  };

  const handleGetProduct = async (event) => {
    event.preventDefault();
    
    let axiosConfig = {
  headers: {
      'Content-Type': 'application/json;charset=UTF-8',
      "Access-Control-Allow-Origin": "*",
  }
  };
    try {
      const response = await axios.get("http://localhost:8000/products/"+productName, axiosConfig);
      alert("Product Details are : "+ JSON.stringify(response.data));
      
    } catch (error) {
      console.error(error);
      alert("GET product has failed : " + error.response.data['msg']);
    }
  };

  const handleAllGetProducts = async (event) => {
    event.preventDefault();
    
    let axiosConfig = {
  headers: {
      'Content-Type': 'application/json;charset=UTF-8',
      "Access-Control-Allow-Origin": "*",
  }
  };
    try {
      const response = await axios.get("http://localhost:8000/products",axiosConfig);
      alert("Product Details are : "+ JSON.stringify(response.data));
      
    } catch (error) {
      console.error(error);
      alert("GET product has failed : " + error.response.data['msg']);
    }
  };

  const handleUsernameChange = (event) => {
    setUsername(event.target.value);
  };

  const handleProductnameChange = (event) => {
    setProductName(event.target.value);
  };

  const handleProductDescChange = (event) => {
    setProductDesc(event.target.value);
  };


  const handleAddOption = async (event) => {
    event.preventDefault();
    setShowProduct(true);
    setShowAdd(false);
    
  };

  const handleGetOption = async (event) => {
    event.preventDefault();
    setShowProduct(true);
    setShowGet(false);
    
  };

  const handleBack = async (event) => {
    event.preventDefault();
    setShowProduct(false);
    setShowAdd(true);
    setShowGet(true);
    
  };


  const handlePasswordChange = (event) => {
    setPassword(event.target.value);
  };

  return (
    <div>
    <div hidden = {showLogin} >
        
          <form method="post" >
          <label>
            Username:
              <input
                type="text"
                id=""
                placeholder="Username"
                name="username"
                required
                value={username}
                onChange={handleUsernameChange}
              />
              </label>
              <label>
                Password
              
              <input
                type="password"
                required
                placeholder="Your Password"
                name="password"
                value={password}
                onChange={handlePasswordChange}
              />
              </label>
          </form>
          <button type="submit" onClick={handleLogin}>
            Log In
          </button>

    </div>

    <div hidden = {showProduct} >
        
          <button type="submit" onClick={handleAddOption}>
           ADD Product 
          </button>
          <button type="submit" onClick={handleGetOption}>
           GET Product 
          </button>
    </div>

    <div hidden = {showAdd} >
    <form method="post" >
          <label>
            Username:
              <input
                type="text"
                id=""
                placeholder="ProductName"
                name="productName"
                required
                value={productName}
                onChange={handleProductnameChange}
              />
              </label>
              <label>
                Password
              
              <input
                type="text"
                required
                placeholder="Product Description"
                name="productDesc"
                value={productDesc}
                onChange={handleProductDescChange}
              />
              </label>
          </form>

          <button type="submit" onClick={handleAddProduct}>
           ADD Product 
          </button>
          <button type="submit" onClick={handleBack}>
           Back
          </button>
          
    </div>

    <div hidden = {showGet} >
    <form method="get" >
          <label>
            Username:
              <input
                type="text"
                id=""
                placeholder="ProductName"
                name="productName"
                required
                value={productName}
                onChange={handleProductnameChange}
              />
              </label>
          </form>

          <button type="submit" onClick={handleGetProduct}>
           GET Product 
          </button>
          <button type="submit" onClick={handleAllGetProducts}>
           GET ALL Products
          </button>
          <button type="submit" onClick={handleBack}>
           Back
          </button>
          
    </div>

    </div>
  );

}

export default Login;