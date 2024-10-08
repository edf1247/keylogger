import React, {useState, useEffect} from 'react'

export default function App(){

    const [data, setData] = useState([{}])

    useEffect(() => {
      fetch("/view_data").then(
        res => res.json()
      ).then(
        data => {
          setData(data)
          console.log(data)
        }
      )
    }, [])

    return(
      <>
        <h1>Pwned System Info</h1>
      </>
    ) 

}