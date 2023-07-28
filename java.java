import java.io.IOException;
import javax.servlet.http.*;

public class VulnerableServlet extends HttpServlet {
    protected void doGet(HttpServletRequest request, HttpServletResponse response)
            throws IOException {
        String name = request.getParameter("name");
        response.setContentType("text/html");
        response.getWriter().println("<h1>Hello, " + name + "!</h1>");
    }
}
