%global debug_package %{nil}
%define _cabal_setup Setup.lhs
%define module HTTP

Summary:	A library for client-side HTTP for Haskell
Name:		ghc-%{module}
Version:	4000.2.6
Release:	3
License:	BSD
Group:		Development/Other
Url:		http://hackage.haskell.org/package/%{module}
Source0:	http://hackage.haskell.org/packages/archive/%{module}/%{version}/%{module}-%{version}.tar.gz
Source10:	%{name}.rpmlintrc
BuildRequires:	ghc-devel
BuildRequires:	haddock
BuildRequires:	haskell-macros
BuildRequires:	haskell(mtl)
BuildRequires:	haskell(network)
BuildRequires:	haskell(parsec)
Requires(post,preun):	ghc
Requires(pre):	haskell(mtl)
Requires(pre):	haskell(network)
Requires(pre):	haskell(parsec)
Obsoletes:	haskell-%{module} < 4000.2.6-2

%description
The HTTP package supports client-side web programming in Haskell. It lets you
set up HTTP connections, transmitting requests and processing the responses
coming back, all from within the comforts of Haskell. It's dependent on the
network package to operate, but other than that, the implementation is all
written in Haskell.

A basic API for issuing single HTTP requests + receiving responses is provided.
On top of that, a session-level abstraction is also on offer  (the
@BrowserAction@ monad); it taking care of handling the management of persistent
connections, proxies, state (cookies) and authentication credentials required
to handle multi-step interactions with a web server.

The representation of the bytes flowing across is extensible via the use of a
type class, letting you pick the representation of requests and responses that
best fits your use.  Some pre-packaged, common instances are provided for you
(@ByteString@, @String@.)

%files
%{_docdir}/%{module}-%{version}
%{_libdir}/%{module}-%{version}
%{_cabal_rpm_deps_dir}
%{_cabal_haddoc_files}

#----------------------------------------------------------------------------

%prep
%setup -q -n %{module}-%{version}

%build
%_cabal_build

%install
%_cabal_install
%_cabal_rpm_gen_deps
%_cabal_scriptlets

