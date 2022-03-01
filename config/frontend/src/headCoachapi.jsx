import React, { useState, useEffect } from 'react';
import axios from 'axios';

import "./css/reset.css"
import "./css/headcoachapi.css"

const HeadCoachAPI = () => {
    const [coachers, setcoachers] = useState([]);

    useEffect(() => {
        axios.get("http://127.0.0.1:8000/api/headcoachers/")
            .then(res => {
                console.log("status:", res.status)
                console.log("axios-data:", res.data)
                setcoachers(res.data)
            })
            .catch(err => {
                console.log("axiosGetErr", err)
            })
    }, [])

    return ( 
        <div className="coachercard-list">
            <ul>
                {
                coachers.map(coacher =>
                        <li className="coachercard" key={ coacher.id }>
                            <img className="coacher-img" src={coacher.headcoachimage} />
                            <p>{ coacher.headcoachname }</p>
                        </li>
                    )
                }
            </ul> 
        </div>
    )
}

export default HeadCoachAPI;