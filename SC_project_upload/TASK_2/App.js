// Filename - App.js
 
import React, { Component } from "react";
import axios from "axios";

class App extends Component {
    render() {
        let heading = ["Name", "Extensions", "Extension Pattern","RansomNote Filenames", "Comment", "Encryption Algorithm","Decryptor", "Resources", "Screenshots"];
        let axiosConfig = {
            headers: {
                'Content-Type': 'application/json;charset=UTF-8',
                "Access-Control-Allow-Origin": "*",
            }
          
          };
          let body = [];
          try {
                const response = axios.get("http://localhost:8000/ransoms", axiosConfig);
                
                let body = (response.json());
              } 
          catch (error) {
                console.error(error);
                alert("GET data has failed ");
              }
          
        return (
            <div>
                <Table heading={heading} body={body} />,
            </div>
        );
    }
}
 
class Table extends Component {
    render() {
        let heading = this.props.heading;
        let body = this.props.body;
        return (
            <table style={{ width: 500 }}>
                <thead>
                    <tr>
                        {heading.map((head, headID) => (
                            <th key={headID}>{head}</th>
                        ))}
                    </tr>
                </thead>
                <tbody>
                    {body.map((rowContent, rowID) => (
                        <TableRow
                            rowContent={rowContent}
                            key={rowID}
                        />
                    ))}
                </tbody>
            </table>
        );
    }
}
 
class TableRow extends Component {
    render() {
        let row = this.props.rowContent;
        return (
            <tr>
                {row.map((val, rowID) => (
                    <td key={rowID}>{val}</td>
                ))}
            </tr>
        );
    }
}
 
export default App;