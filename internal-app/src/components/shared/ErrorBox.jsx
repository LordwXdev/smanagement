"use client";
export default function ErrorBox({ message, onRetry }) {
  return (
    <div style={{padding:24,background:"#fef2f2",borderRadius:12,border:"1px solid #fecaca",margin:"16px 0"}}>
      <div style={{color:"#dc2626",fontWeight:600,marginBottom:8}}>Something went wrong</div>
      <div style={{color:"#7f1d1d",fontSize:14}}>{message}</div>
      {onRetry && <button onClick={onRetry} style={{marginTop:12,padding:"8px 20px",background:"#dc2626",color:"white",border:"none",borderRadius:8,cursor:"pointer",fontSize:13,fontWeight:600}}>Retry</button>}
    </div>
  );
}
