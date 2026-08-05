import { cn } from "@/lib/utils";
import React from "react";

interface CardProps extends React.HTMLAttributes<HTMLDivElement> {
  children: React.ReactNode;
}

export const Card = ({ className, children, ...props }: CardProps) => (
  <div 
    className={cn(
      "rounded-2xl border border-[#1E1E1E] bg-[#111111]/80 backdrop-blur-sm p-6 shadow-xl", 
      className
    )} 
    {...props}
  >
    {children}
  </div>
);

export const Button = ({ className, ...props }: React.ButtonHTMLAttributes<HTMLButtonElement>) => (
  <button
    className={cn(
      "inline-flex items-center justify-center rounded-lg bg-indigo-600 px-4 py-2 text-sm font-medium text-white transition-colors hover:bg-indigo-700 disabled:opacity-50",
      className
    )}
    {...props}
  />
);
