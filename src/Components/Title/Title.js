import React, { Component } from 'react';
import './Title.css';

class Title extends Component{
    render(){
        return(
            <React.Fragment>
                <h1 className="Heading">Optical Character Recognition</h1>
                <h3>Software Group Project</h3>
                <h4>Semester: 5</h4>
            </React.Fragment>
        );
    }
}

export default Title;