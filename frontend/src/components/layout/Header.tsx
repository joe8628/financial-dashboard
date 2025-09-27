import React from 'react'
import { useAuthStore } from '../../stores/authStore'

const Header: React.FC = () => {
  const { user, isAuthenticated } = useAuthStore()

  return (
    <header className="bg-white shadow-sm border-b border-gray-200">
      <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
        <div className="flex justify-between items-center h-16">
          <div className="flex items-center">
            <h1 className="text-xl font-bold text-gray-900">
              Financial Dashboard
            </h1>
          </div>
          
          {isAuthenticated && user && (
            <div className="flex items-center space-x-4">
              <span className="text-sm text-gray-700">
                Welcome, {user.first_name || user.username}
              </span>
            </div>
          )}
        </div>
      </div>
    </header>
  )
}

export default Header