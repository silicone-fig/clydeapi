import React from 'react';
import Head from 'next/head';

const Layout: React.FC = ({ children }) => {
  return (
    <div>
      <Head>
        <link rel="stylesheet" href="/globals.css" />
      </Head>
      {children}
    </div>
  );
};

export default Layout;
