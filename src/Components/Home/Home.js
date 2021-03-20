import React, {Component} from 'react';
import Title from '../Title/Title';
import Container from '../Container/Container';
import Description from '../Description/Description';

class Home extends Component{
    render(){
        return(
            <React.Fragment>
                <Title />
                <Container />
                <Description />
            </React.Fragment>
        );
    }
}

export default Home;