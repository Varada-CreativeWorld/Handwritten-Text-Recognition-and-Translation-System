import React from 'react';
import Home from './Components/Home/Home';
import { BrowserRouter as Router, Route} from 'react-router-dom';
import './App.css';

function App() {
  return (
    <div className="App">
      <Router>
        <Route exact path='/' component={Home}></Route>
        {/* <Route exact path='/hindiChar' component={}></Route> */}
      </Router>
    </div>
  );
}

export default App;
