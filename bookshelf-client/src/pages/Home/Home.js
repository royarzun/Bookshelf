import React from "react";
import { Link } from "react-router-dom";
import { BOOKS } from "../../constants/routes";

const Home = () => {
  return (
    <div className="min-h-screen flex items-center justify-center bg-gray-50 py-12 px-4 sm:px-6 lg:px-8">
      <div className="max-w-md w-full">
        <div>
          <h1 className="text-6xl text-center">
            <span role="img" aria-label="books">
              📚
            </span>
          </h1>
        </div>
        <div className="mt-6">
          <Link
            to={BOOKS}
            className="group relative w-full flex justify-center py-2 px-4 border border-transparent text-sm font-medium rounded-md text-white bg-teal-600 hover:bg-teal-500 focus:outline-none focus:border-teal-700 focus:shadow-outline-teal active:bg-teal-700 transition duration-150 ease-in-out"
          >
            <span className="absolute left-0 inset-y pl-3">
              <svg
                className="h-5 w-5 text-teal-500 group-hover:text-teal-400 transition ease-in-out duration-150"
                fill="currentColor"
                viewBox="0 0 20 20"
              >
                <path
                  fillRule="evenodd"
                  d="M5 9V7a5 5 0 0110 0v2a2 2 0 012 2v5a2 2 0 01-2 2H5a2 2 0 01-2-2v-5a2 2 0 012-2zm8-2v2H7V7a3 3 0 016 0z"
                  clipRule="evenodd"
                />
              </svg>
            </span>
            Sign in
          </Link>
        </div>
      </div>
    </div>
  );
};

export default Home;