"use client";
import { useState } from "react" ;

export default function EditInfoPage() {
    const [fullName, setFullName] = useState("");
    const [Nickname, setNickName] = useState("");
    const [ContactInfo, setContactInfo] = useState("");
    const [goingHome, setGoingHome] = useState<"parents" | "other">("parents");
    const [address, setAddress] = useState("");

    return (
        <div className="min-h-screen bg-black text-white px-6 py-8">
            <button className="flex items-center gap-2 text-gray-400 hover:text-white transition-colors">
                <span className="text-lg">←</span>
                <span>Back</span>
            </button>


            {/* Header */}
            <div className="flex items-center gap-3 mt-8 mb-10">
                <span className="text-3xl">⚽</span>
                <h1 className="text-5xl font-black bold tracking-tight">
                    EDIT INFO
                </h1>
            </div>
            

            {/* Fullname */}
            <div className="flex flex-col gap-7"></div>
                <div>
                    <label className="block font-bold mb-2">Full name</label>
                    <input
                        type="text"
                        value={fullName}
                        onChange={(e) => setFullName(e.target.value)}
                        className="w-full bg-[#1c1f2e] rounded-l px-4 py-4 outline-none focus:ring-2 focus:ring-yellow-500"
                    />
                </div>


            {/* Nickname */}
            <div className="flex flex-col gap-7"></div>
                <div>
                    <label className="block font-bold mb-2">Nickname</label>
                    <input
                        type="text"
                        value={Nickname}
                        onChange={(e) => setNickName(e.target.value)}
                        className="w-full bg-[#1c1f2e] rounded-l px-4 py-4 outline-none focus:ring-2 focus:ring-yellow-500"
                    />
                </div>


            {/* Contact info */}
            <div className= "flex f;ex-col gap-7"></div>
                <div>
                    <label className="block font-bold mb-2">Contact info</label>
                    <input
                        type="text"
                        value={ContactInfo}
                        onChange={(e) => setContactInfo(e.target.value)}
                        className="w-full bg-[#1c1f2e] rounded-l px-4 py-4 outline-none focus:ring-2 focus:ring-yellow-500"
                    />
                </div>


            {/* Going home */}
            <div className="flex flex-col gap-1">
                <label className="block font-bold mb-3">
                    How are you going home?
                </label>

                <div>
                    <label className="flex items-center gap-3 cursor-pointer">
                    <input
                        type="radio"
                        name="goingHome"
                        checked={goingHome === "parents"}
                        onChange={() => setGoingHome("parents")}
                        className="appearance-none w-6 h-6 rounded-full border-2 border-gray-500 checked:bg-yellow-500 checked:ring-4 checked:ring-inset checked:ring-black relative cursor-pointer"
                    />
                    <span>Parents</span>
                    </label>

                    <label className="flex items-center gap-3 cursor-pointer">
                        <input
                            type="radio"
                            name="goingHome"
                            checked={goingHome === "other"}
                            onChange={() => setGoingHome("other")}
                            className="appearance-none w-6 h-6 rounded-full border-2 border-gray-500 checked:bg-yellow-500 checked:ring-4 checked:ring-inset checked:ring-black relative cursor-pointer"
                        />
                    <span>Other (Please include address incase of emergency)</span>
                    </label>
                    
                    {/* Conditional address */}
                    {goingHome === "other" && (
                    <input
                        type="text"
                        placeholder="Emergency address"
                        value={address}
                        onChange={(e) => setAddress(e.target.value)}
                        className="w-full bg-[#1c1f2e] rounded-xl px-4 py-4 outline-none focus:ring-2 focus:ring-yellow-500 ml-9"
                    />
                    )}

                </div>
            </div>

            {/* Confirm button */}
            <button
                // onClick={variable}
                // connec to back
                className="flex items-center justify-center bg-yellow-500 hover:bg-yellow-400 transition-colors text-black font-extrabold text-lg rounded-2xl py-4 mt-4"
            >
            CONFIRM
            </button>

        </div>
    );
}