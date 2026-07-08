"use client";

import { useState } from "react";

export default function RegisterPage() {
    const [selected, setSelected] = useState("");
    return (
        <main className="min-h-screen bg-[#0B0B10] flex justify-center px-6 py-12">
        <div className="w-full max-w-xl p-8">
            <a href="../page.tsx"><button className="mb-3 text-gray-500 hover:text-white">&#8592; Back</button></a>
            <h1 className="mb-6 text-5xl font-bold text-center">⚽ REGISTER</h1>

            <div className="flex flex-col gap-6">
                <label>Username</label>
                <input
                type="text"
                className="w-full rounded-2xl focus:outline-none border p-3"
                />

                <label>Password</label>
                <input
                type="password"
                className="rounded border p-3"
                />

                <label>Confirm Password</label>
                <input
                type="password"
                className="rounded border p-3"
                />

                <label>Full name</label>
                <input
                type="text"
                className="rounded border p-3"
                />

                <label>Nickname</label>
                <input
                type="text"
                className="rounded border p-3"
                />

                <label>Contact info</label>
                <input
                type="text"
                className="rounded border p-3"
                />

                <p>How are you going home?</p>
                <label><input type="radio" name="source" value="parents" onChange={(e) => setSelected(e.target.value)} className="rounded border p-3"/> Parents</label>
                <label><input type="radio" name="source" value="other" onChange={(e) => setSelected(e.target.value)} className="rounded border p-3"/> Other</label>
                {selected === "other" && (
                    <input
                        type="text"
                        placeholder="Please include address incase of emergencies"
                        className="rounded border p-3"
                    />
                )}
                <label className="flex items-center gap-3"><input type="checkbox" /> I accept and understand the rules</label>
                <button className="rounded bg-green-600 p-3 text-black hover:bg-green-700">REGISTER</button>
            </div>
        </div>
        </main>
    );
}