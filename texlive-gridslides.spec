%global tl_name gridslides
%global tl_revision 54512

Name:		texlive-%{tl_name}
Epoch:		1
Version:	0.1.1
Release:	%{tl_revision}.1
Summary:	Free form slides with blocks placed on a grid
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/gridslides
License:	lppl1.3 gpl2
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/gridslides.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/gridslides.doc.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
This package allows creating free form slides with blocks placed on a
grid. The blocks can be filled with text, equations, figures etc. The
resulting slides are similar to the ones produced with LaTeX beamer, but
more flexible. Sequential unconvering of elements is supported. A
compiler script is provided which compiles each slide separately, this
way avoiding long compile times.

