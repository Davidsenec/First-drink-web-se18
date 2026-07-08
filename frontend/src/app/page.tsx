export default function Home() {
  return (
    <div className="flex flex-col min-h-screen items-center justify-center">
      <div className="flex flex-col text-center">
        <div>Image</div>
        <div className="text-[#5b6c82]">
          First Drink
        </div>
        <div className="text-[#f0990d]">
          Software Engineering
        </div>
      </div>
      <div>
        Login
      </div>
      <input
      type="text"
      placeholder="Username"
      />
      <input
      type="text"
      placeholder="Password"
      />
      <button className="text-[#f0990d]">
        Login
      </button>
      <div className='text-[#5b6c82]'>
        New here? <a href="register/page.tsx" className='text-[#f0990d]'>Sign up here</a>
      </div>
    </div>
  );
}
