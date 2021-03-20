import React, { Component } from 'react';
import './Container.css';
import UploadImage from '../UploadImage/UploadImage';

class Container extends Component{
    render(){
        return(
            <div className="ContainerStyle">
                <UploadImage />      
                <br></br>          
                <p className="output"> {window.token}</p>
            </div>
        );
    }
}

export default Container;