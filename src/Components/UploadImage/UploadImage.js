import React, { Component } from 'react';
import axios from 'axios';
import { isCompositeComponentWithType } from 'react-dom/test-utils';
import './UploadImage.css';

class UploadImage extends Component {
  constructor(props) {
    super(props);
    this.state = {
      // image: null
      selectedFile: null
    };

    this.fileSelectedHandler = this.fileSelectedHandler.bind(this);
    this.fileUploadHandler = this.fileUploadHandler.bind(this);
  }

  state = {
    selectedFile: null,
    image: null,
    option: null
  }

  fileSelectedHandler = event => {
    this.setState({
      selectedFile: event.target.files[0],      
      image: URL.createObjectURL(event.target.files[0])
    });
  };

  fileUploadHandler = () => {
    const fd = new FormData();
    fd.append('myImage', this.state.selectedFile, this.state.selectedFile.name);
    // var xhttp = new XMLHttpRequest();
    // var apiUrl = "http://127.0.0.1:3000/";
    // xhttp.onreadystatechange = function (){
    //   if(this.readyState === 4 && this.status === 200){
    //     console.log(this.responseText);
    //   }
    // }

    // xhttp.open('POST', apiUrl, true);
    // xhttp.setRequestHeader("Content-type", "application/x-www-form-urlencoded");
    // xhttp.send(fd);

    this.selectedOption();
    
    axios.post('http://127.0.0.1:3000/', fd).catch(error => {
      console.log(error);
    }).then(res => {
      console.log(res);
    });
  };

  selectedOption = () => {
    // var elementSelected = document.getElementById('select1').value;
    // if (elementSelected == 'hindiChar'){
    //   document.getElementById('inpText').style.display = 'none';
    //   document.getElementById('upimg').style.display = 'inline-block';
    // }
    // if( elementSelected == 'h2e'){
    //   document.getElementById('upimg').style.display = 'none';
    //   document.getElementById('inpText').style.display = 'inline-block';
    // }
    document.getElementById('sub').style.display = 'inline-block';
    // const fd = new FormData();
    // fd.append('select1', elementSelected);
    // axios.post('http://127.0.0.1:3000/hindiChar', fd).catch(error => { console.log(error); }).then(res => {console.log(res)});
  };

  render() {
    return (
          <div>
            <img src={this.state.image} />
            <br/>
            <form method="POST" action="#" encType="multipart/form-data">
              <label>Please Upload Your Image Here : </label>
              <input type="file" name="myImage" id="upimg" onChange={this.fileSelectedHandler}/>
              <br /><br />
              <label>Select the language you want to translate into : </label>
              <select id="select1" name="select1" onChange={this.selectedOption}>
                <option selected>Please Choose</option>
                <option value="hindiChar">Hindi Character Recognition</option>
                <option value="hindi">Hindi</option>
                <option value="english">English</option>
              </select>
              <br></br>
              
              <br />
              {/* <label id="inpText">Please enter the text you want to translate: </label> */}
              <br></br>
              <br />
              {/* <input type="text" name="inpText" id="inpText"></input>{'           '} */}
              <input type="submit" value="submit" id="sub" onClick={this.fileUploadHandler} />
              <br/>
            </form>
          </div>
    );
  }
}
export default UploadImage;