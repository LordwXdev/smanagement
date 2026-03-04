import "@/styles/globals.css";
export const metadata = { title: "School Portal", description: "Student & Teacher Portal" };
export default function RootLayout({ children }) {
  return (<html lang="en"><body>{children}</body></html>);
}
