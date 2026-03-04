"use client";
export default function Loading({ text }) {
  return (
    <div style={{display:"flex",alignItems:"center",justifyContent:"center",padding:60,color:"#64748b",fontSize:15}}>
      {text || "Loading..."}
    </div>
  );
}
