import React from "react";
import "./App.css";
import Login from "./components/login";
import SignUp from "./components/signup";

import { BrowserRouter as Router, Route, Link, Routes } from "react-router-dom";
import NoDataPage from "./components/noData";

function App() {
  return (
    <div className="App">
      <Router>
        <Routes>
          <Route path="/" Component={Login}></Route>
          <Route path="/login" Component={Login}></Route>
          <Route path="/signup" Component={SignUp}></Route>
          <Route path="/no-data" Component={NoDataPage}></Route>
        </Routes>
      </Router>
    </div>
  );
}

export default App;
