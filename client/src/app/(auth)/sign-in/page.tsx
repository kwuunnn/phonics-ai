"use client";

import { useRouter } from "next/navigation";
import { useState } from "react";
import { Input } from "@/components/ui/input";
import { Button } from "@/components/ui/button";
import { Label } from "@/components/ui/label";
import Image from "next/image";
import Link from "next/link";

export default function SignIn() {
  const [email, setEmail] = useState("");
  const [password, setPassword] = useState("");
  const router = useRouter();

  // Handle form submission
  const handleForm = async (event: { preventDefault: () => void }) => {
    event.preventDefault();

    // Attempt to sign in with provided email and password
    // const { result, error } = await signIn(email, password);

    if (error) {
      // Display and log any sign-in errors
      console.log(error);
      return;
    }

    // Sign in successful
    console.log(result);

    // Redirect to the admin page
    // Typically you would want to redirect them to a protected page an add a check to see if they are admin or
    // create a new page for admin
    router.push("/");
  };

  return (
    <div className="flex flex-col lg:flex-row items-center justify-center h-screen">
      {/* <Image
        src="/logo.jpg"
        alt="Track My Mods Logo"
        width={300}
        height={300}
        className="m-10"
      /> */}
      <div className="flex flex-col items-center w-full max-w-md">
        <h1 className="text-5xl font-black text-blue-dark">TRACK MY MODS</h1>
        <form
          onSubmit={handleForm}
          className="px-8 pt-6 pb-8 mb-4 flex flex-col items-center w-full max-w-sm"
        >
          <div className="mb-4 w-full">
            <Label htmlFor="email" className="block text-sm font-bold mb-2">
              Email
            </Label>
            <Input
              onChange={(e) => setEmail(e.target.value)}
              required
              type="email"
              name="email"
              id="email"
              placeholder="example@mail.com"
              className="bg-gray-200"
            />
          </div>
          <div className="w-full">
            <Label htmlFor="password" className="block text-sm font-bold mb-2">
              Password
            </Label>
            <Input
              onChange={(e) => setPassword(e.target.value)}
              required
              type="password"
              name="password"
              id="password"
              className="bg-gray-200"
            />
          </div>
          <Button type="submit" className="w-full bg-blue font-semibold my-6">
            Sign In
          </Button>
          <text>
            Don't have an account?{" "}
            <Link href="/sign-up" className="text-blue">
              Create an account
            </Link>
          </text>
        </form>
      </div>
    </div>
  );
}
