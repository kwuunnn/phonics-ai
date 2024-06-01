"use client";

import { useRouter } from "next/navigation";
import { useState } from "react";
import { Input } from "@/components/ui/input";
import { Button } from "@/components/ui/button";
import { Label } from "@/components/ui/label";
import Image from "next/image";
import Link from "next/link";

export default function SignUp() {
  const [email, setEmail] = useState("");
  const [username, setUsername] = useState("");
  const [password, setPassword] = useState("");
  const router = useRouter();

  // Handle form submission
  const handleForm = async (event: { preventDefault: () => void }) => {
    event.preventDefault();

    // Attempt to sign up with provided email and password
    // const { result, error } = await signUp(email, password);

    if (error) {
      // Display and log any sign-up errors
      console.log(error);
      return;
    }

    // Sign up successful
    console.log(result);

    // Redirect to the home page
    router.push("/home");
  };

  return (
    <div className="flex flex-col items-center justify-center h-screen">
      <div className="flex flex-col items-center w-full max-w-md">
        <div className="flex flex-row items-center">
          <h1 className="text-5xl font-black text-blue-dark">Sign Up</h1>
          {/* <Image
            src="/logo.jpg"
            alt="Track My Mods Logo"
            width={50}
            height={50}
            className="ml-5"
          /> */}
        </div>
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
          <div className="mb-4 w-full">
            <Label htmlFor="username" className="block text-sm font-bold mb-2">
              Username
            </Label>
            <Input
              onChange={(e) => setUsername(e.target.value)}
              required
              type="username"
              name="username"
              id="username"
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
            Sign Up
          </Button>
          <text>
            Already have an account?{" "}
            <Link href="/sign-in" className="text-blue">
              Sign In
            </Link>
          </text>
        </form>
      </div>
    </div>
  );
}
