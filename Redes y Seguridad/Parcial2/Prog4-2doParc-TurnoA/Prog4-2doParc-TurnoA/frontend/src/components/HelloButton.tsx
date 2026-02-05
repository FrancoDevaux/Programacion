import { useState } from "react";

export default function HelloButton() {
  const [show, setshow] = useState(false);
  return (
    <>
      {show && <p> Hola mundo</p>}
      <button onClick={() => setshow(!show)}> Mostrar Mensaje </button>
    </>
  );
}