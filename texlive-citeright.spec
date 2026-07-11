%global tl_name citeright
%global tl_revision 75480

Name:		texlive-%{tl_name}
Epoch:		1
Version:	1.0.0
Release:	%{tl_revision}.1
Summary:	Specify accurate natbib citations for diverse naming conventions
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/citeright
License:	lppl1.3c
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/citeright.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/citeright.doc.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
This package provides the command \citeright for aliasing in-text
citations and specifying their appearance in the list of references. It
is specifically tailored for use with the natbib package and is
compatible with citation managers such as BibDesk and JabRef. The
package is intended to provide a means for respecting the diverse naming
conventions of cited authors and, in this way, decolonizing academia.

